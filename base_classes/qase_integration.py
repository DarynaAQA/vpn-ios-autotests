import datetime
import requests
import os
from dotenv import load_dotenv


class QASEIntegration:

    load_dotenv()

    headers = {
        "Token": os.getenv("API_TOKEN"),
        "accept": "application/json",
        "content-type": "application/json"
    }

    def create_test_run(self, test_plan_id: int):
        """
            This method create new test run id. It accepts specific test plan id in integer format.
        """
        url = "https://api.qase.io/v1/run/PI"

        date = datetime.datetime.today().strftime("%d.%m.%Y(%H:%M)")

        payload = {
            "title": f"Debug_Testing_Mobile_iOS_{date}",
            "plan_id": test_plan_id
        }

        result_request = requests.post(url, json=payload, headers=self.headers)
        response_test = result_request.json()
        test_run_id = response_test['result']['id']
        return test_run_id

    def create_passed_result(self, case: int, test_run_id: int, time: int):
        """
            This method transfer positive result of execute test case. It accepts specific test run id, the test case id
            and time of execute the test case.
        """
        url = f"https://api.qase.io/v1/result/PI/{test_run_id}"

        payload = {
            "status": "passed",
            "case_id": case,
            "time_ms": f"{int(time) * 1000}"
        }

        response = requests.post(url, json=payload, headers=self.headers)
        print(response.text)
        return case

    def create_failed_result(self, case: int, test_run_id: int, time: int, comment):
        """
            This method transfer negative result of execute test case. It accepts specific test run id, the test case id
            and time of execute the test case.
        """
        url = f"https://api.qase.io/v1/result/PI/{test_run_id}"

        payload = {
            "status": "failed",
            "case_id": case,
            "time_ms": f"{int(time) * 1000}",
            "comment": comment

        }

        response = requests.post(url, json=payload, headers=self.headers)
        print(response.text)
        return case

    def update_publicity_test_run(self, test_run_id: int):
        """
            This method makes the test run public.
        """
        url = f"https://api.qase.io/v1/run/PI/{test_run_id}/public"

        payload = {
            "status": True
        }
        response = requests.patch(url, json=payload, headers=self.headers)
        response_json = response.json()
        public_test_run_url = response_json['result']['url']
        return public_test_run_url

    def send_test_run_url_to_slack(self, public_test_run_url: str, test_time) -> int:
        """
            This method send public url with test run result to Slack channel "qa-qase-results".
        """
        date = datetime.datetime.today().strftime("%d.%m.%Y")
        payload = {"blocks":
            [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":gear: <{public_test_run_url}|*Debug_iOS_testing_{date}({test_time})*>\n "
                            f"В случае проблемы обращаться к <@U03LV5XPYCX>"
                }}]}

        headers = {
            "content-type": "application/json"
        }

        load_dotenv()
        slack_url = os.getenv("SLACK_URL_GIT")
        response = requests.post(slack_url, json=payload, headers=headers)
        return response.status_code



