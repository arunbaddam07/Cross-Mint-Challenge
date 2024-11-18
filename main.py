import requests
import json
import time

def get_goal_map(candidate_id):
    """
    Fetches the goal map matrix for the current challenge phase.

    Parameters:
            candidate_id (str): A string

    Returns:
            matrix (list of lists): Goal map converted into a matrix with celestial objects in the order
    """
    api_url = f"https://challenge.crossmint.io/api/map/{candidate_id}/goal"
    response = requests.get(api_url)
    print("Full Response JSON:")
    print(response.json())  # Print the full JSON response to understand its structure

    try:
        goal_map = response.json()["goal"]
        return goal_map
    except KeyError:
        print(
            "Key 'goal' not found in the response. Check the JSON structure printed above."
        )
        return None


def post_polyanets(candidate_id, row, col, astral = "SPACE", parameter = None,key = None):
    """
    Make a POST request to create a polyanet at a particular position.

    Parameters:
        candidate_id (str): A string
        row (int): Row index where the polyanet will be placed
        col (int): Column index where the polyanet will be placed
    """
    api_url = "https://challenge.crossmint.io/api/" + astral.lower() + 's'
    print("API URL:", api_url)
    if key:
        data = {"row": row, "column": col, "candidateId": candidate_id, key: parameter}
    else:
        data = {"row": row, "column": col, "candidateId": candidate_id}
    print("Data:", data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    #response = requests.delete(api_url, data=json.dumps(data), headers=headers)

    print(f"Posted polyanet at ({row}, {col}) with response {response.status_code}")


def create_shape_from_map(candidate_id, matrix):
    """
    Creates a shape based on the goal map matrix.

    Parameters:
        candidate_id (str): A string representing the candidate's ID.
        matrix (list of lists): The matrix representing the goal map.
    """
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "POLYANET":  # Assuming 'P' denotes the positions for polyanets in the goal map
                post_polyanets(candidate_id, i, j, astral="POLYANET")
                time.sleep(1)
            elif cell == "SPACE":
                continue
            else:
                parameter, astral = cell.split("_")
                if astral == "SOLOON":
                    post_polyanets(candidate_id, i, j, astral, parameter.lower(),'color')
                    time.sleep(1)
                elif astral == "COMETH":
                    post_polyanets(candidate_id, i, j, astral, parameter.lower(),'direction')
                    time.sleep(1)


def main():
    candidate_id = "7ec04af7-0fdb-47dc-a81b-b643ac55a1ca"  # Change this to your actual candidate ID
    goal_map = get_goal_map(candidate_id)
    if goal_map:
        create_shape_from_map(candidate_id, goal_map)


if __name__ == "__main__":
    main()
