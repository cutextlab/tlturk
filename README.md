# `tlturk`: TextLab's Custom MTurk API

## Basic Usage

1. Install by running `pip install git+https://github.com/jpowerj/tlturk.git`
2. Import it into your python file by including `import tlturk` at the top of the file
3. Create an AMT access key configuration file, `access_keys.conf`, with the following format, and save it somewhere secure:
    ```
    [AMT_Keys]
    ACCESS_KEY=<your access key here>
    SECRET_KEY=<your secret key here>
    ```
4. Before using any other function, call `tlturk.load_keys(<path to config file>)`. So, for example, if your `access_keys.conf` file is in the same folder as the .py file you're writing, just call `tlturk.load_keys("access_keys.conf")`.
5. Now you can use any of the API's functions! Specifically:
    * `assign_qualification(qual_id, worker_id, score)`: Assigns the qualification with id `qual_id` to the worker with id `worker_id`, with the qualification's "score" parameter set to `score` (an integer).
    * `get_balance()`: Returns your account's current balance as a string (e.g., '25.00' for a $25 balance). Use `float(get_balance())` to get your balance as a Python float instead.
    * `get_hit(hit_id)`: Returns the information AMT provides for the HIT with id `hit_id`.
    * `grant_bonus(worker_id, assignment_id, amount, reason)`: Awards a bonus with amount `amount` (a float value, e.g. 0.01 to award a 1-cent bonus) to the worker with id `worker_id`, for their work on the assignment with id `assignment_id`, and
    with a string explaining the award, `reason`. Note that this function does
    *NOT* raise any Exceptions if something goes wrong, it just returns `False`. I
    wrote it this way so that if one bonus fails it doesn't derail an entire
    loop, or whatever external script called the function.
    * `revoke_qualification(qual_id, worker_id)`: Removes the qualification with id `qual_id` from the worker with id `worker_id`.

Contact me (Jeff) at jpj2122@columbia.edu with any questions!