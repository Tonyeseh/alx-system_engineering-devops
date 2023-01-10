# 0x12. Web stack debugging #2
Important lessons in this project
* Do not run your server as root
* If a service does not run, sometimes another service is using it's port.
* Also, you should check if the config file is valid.

## Tasks :page_with_curl:

* 0. Run software as another user
	* [0-iamsomeoneelse](./0-iamsomeoneelse): takes in one arg and executes `whoami` user the user passed as arg
* 1. Run Nginx as Nginx
	* [1-run_nginx_as_nginx](./1-run_nginx_as_nginx): configures `nginx` to run as `nginx` user and listens on port `8080`
* 2. 7 lines or less
	* [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less): does the same thing with `task 1`
