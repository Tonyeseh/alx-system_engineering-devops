# 0x04 Loops, conditions and parsing
###### Learnt about loops, variable assignment and arithmetic, comparison operators, file test operators, how to make scripts portable... The commands lerant are `env`, `cut`, `for`, `while`, `until`, `if` and `awk` for the advanced task.

## Tasks :page_with_curl:

* **0. Create a SSH RSA key pair**
	* [0-RSA_public_key.pub](./0-RSA_public_key.pub) - contains the public key a intranet machine

* **1. For Best School loop**
	* [1-for_best_school](./1-for_best_school) - displays `Best School` 10 times using `for` loop

* **2. While Best School loop**
	* [2-while_best_school](./2-while_best_school) - displays `Best School` 10 times using `while` loop

* **3. Until Best School loop**
	* [3-until_best_school](./3-until_best_school) - Bash script that displays `Best School` 10 times using `until`

* **4. If 9, say Hi!**
	* [4-if_9_say_hi](./4-if_9_say_hi) - Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.
	* Using only `while` loop and `if` statement

* **5. 4 bad luck, 8 is your chance**
	* [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance) - Bash script that loops from 1 to 10 and:
		* displays `bad luck` for the 4th loop iteration
		* displays `good luck` for the 8th loop iteration
		* displays `Best School` for the other iterations
	* Using `while` loop and `if`, `elif` and `else` statements

* **6. Superstitious numbers**
	* [6-superstitious_numbers](./6-superstitious_numbers) - Bash script that displays numbers from 1 to 20 and:
		* displays `4` and then `bad luck from China` for the 4th loop iteration
		* displays `9` and then `bad luck from Japan` for the 9th loop iteration
		* displays `17` and then `bad luck from Italy` for the 17th loop iteration
	* Using `while` loop and `case` statement

* **7. Clock**
	* [7-clock](./7-clock) - Bash script that displays the time for 12 hours and 59 minutes:
		* display hours from 0 to 12
		* display minutes from 1 to 59
	* Using `while` loop

* **8. For ls**
	* [8-for_ls](./8-for_ls) - Bash script that displays:
		* The content of the current directory
		* In a list format
	* Using `for` loop

* **9. To file, or not to file**
	* [9-to_file_or_not_to_file](./9-to_file_or_not_to_file) - Bash script that gives you information about the `school` file.
	* check if the file exists and print:
		* if the file exists: school file exists
		* if the file does not exist: school file does not exist
	* If the file exists, print:
		* if the file is empty: school file is empty
		* if the file is not empty: school file is not empty
		* if the file is a regular file: school is a regular file
		* if the file is not a regular file: (nothing)

* **10. FizzBuzz**
	* [10-fizzbuzz](./10-fizzbuzz) - Bash script that displays numbers from 1 to 100.
	* Displays FizzBuzz when the number is a multiple of 3 and 5
	* Displays Fizz when the number is multiple of 3
	* Displays Buzz when the number is a multiple of 5
	* Otherwise, displays the number

* **11. Read and cut**
	* [100-read_and_cut](./100-read_and_cut) - Bash script that displays the content of the file `/etc/passwd`.

* **12. Tell the story of passwd**
	* []() - Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + `IFS`.
	* Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

* **13. Let's parse Apache logs**
	* [102-lets_parse_apache_logs](./102-lets_parse_apache_logs) - Bash script that displays the visitor IP along with the HTTP status code from the [Apache log file](./apache-access.log) using `awk`
	* Format: IP HTTP_CODE

* **14. Dig the data**
	* [103-dig_the-data](./103-dig_the-data) - Bash script that groups visitors by IP and HTTP status code, and displays this data using `awk`.
	* Format: OCCURENCE_NUMBER IP HTTP_CODE
