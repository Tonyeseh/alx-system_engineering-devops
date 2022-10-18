# 0x06. Regular expression
In this project I learnt Regular expression using Ruby's Oniguruma library.

## Tasks :page_with_curl:
_Note: Each script in this project maches regular expressions based on the argument passed to it through the command line._

* **0. Simply matching School**
	* [0-simply_match_school.rb](./0-simply_match_school.rb) - Matches the regular expression `School`.

* **1. Repetition Token #0**
	* [1-repetition_token_0.rb](./1-repetition_token_0.rb) - matches the regular expression `hb` with 2-5 number of `t`s and an `n`.

* **2. Repetition Token #1**
	* [2-repetition_token_1.rb](./2-repetition_token_1.rb) - Matches the regular expression `h` followed by no or 1 `b` and a `t` and `n`.

* **3. Repetition Token #2**
	* [3-repetition_token_2.rb](./3-repetition_token_2.rb) - Matches the `hb` followed by 1 or more `t`s and an `n`.

* **4. Repetition Token #3**
	* [4-repetition_token_3.rb](./4-repetition_token_3.rb) - Matches the expression hb followed by no or more than one ts and an n.

* **5. Not quite HBTN yet**
	* [5-beginning_and_end.rb](./5-beginning_and_end.rb) - Matches a string that starts with `h` ends with `n` and can have any single character in between.

* **6. Call me maybe**
	* [6-phone_number.rb](./6-phone_number.rb) - Matches a 10 digit phone number that has nothing but digits.

* **7. OMG WHY ARE YOU SHOUTING?**
	* [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb) - Matches only capital letters.
* **8. Textme**
	* [100-textme.rb](./100-textme.rb) - Script that runs statistics on TextMeapp text message transactions.
	* Output: `[SENDER],[RECEIVER],[FLAGS]` where
		* `[SENDER]` is the sender phone number or name (including country code if present).
		* `[RECEIVER]` is the receiver phone number or name (including country code if present).
		* `[FLAGS]` is the flags that were used.
