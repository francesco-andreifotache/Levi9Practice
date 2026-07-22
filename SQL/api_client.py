from dataclasses import dataclass

import requests

from settings import get_api_base_url


@dataclass
class ApiResponse:
    success: bool
    message: str


class APIClient:

    @staticmethod
    def test_connection(endpoint: str = "/genres") -> ApiResponse:

        try:
            url = get_api_base_url() + endpoint

            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return ApiResponse(
                    success=True,
                    message=f"Connected successfully to {url}"
                )

            return ApiResponse(
                success=False,
                message=f"API returned status code {response.status_code}"
            )

        except requests.exceptions.ConnectionError:
            return ApiResponse(
                success=False,
                message=f"Could not connect to {url}"
            )

        except requests.exceptions.Timeout:
            return ApiResponse(
                success=False,
                message="Request timed out"
            )

        except Exception as e:
            return ApiResponse(
                success=False,
                message=str(e)
            )

    @staticmethod
    def get(endpoint: str):

        try:
            url = get_api_base_url() + endpoint

            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return response.json(), None

            return None, f"Error {response.status_code}"

        except Exception as e:
            return None, str(e)

    @staticmethod
    def post(endpoint, data):
        try:

            response = requests.post(
                f"{get_api_base_url()}{endpoint}",
                json=data
            )

            if response.status_code in (200, 201):
                return response.json(), None

            try:
                error = response.json()
                return None, str(error)
            except:
                return None, f"Error {response.status_code}"

        except Exception as e:
            return None, str(e)

    @staticmethod
    def put(endpoint, data):

        try:
            response = requests.put(
                f"{get_api_base_url()}{endpoint}",
                json=data
            )

            if response.status_code == 200:
                return response.json(), None

            try:
                return None, response.json()
            except:
                return None, f"Error {response.status_code}"

        except Exception as e:
            return None, str(e)

    @staticmethod
    def delete(endpoint):

        try:
            response = requests.delete(
                f"{get_api_base_url()}{endpoint}"
            )

            if response.status_code in (200, 204):
                return True, None

            try:
                return False, response.json()
            except:
                return False, f"Error {response.status_code}"

        except Exception as e:
            return False, str(e)