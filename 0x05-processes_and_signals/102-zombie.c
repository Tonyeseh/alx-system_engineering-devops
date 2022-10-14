#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


/**
 * infinite_while - infinite loop
 *
 * Return: 0 Always
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Create 5 zombie processess
 *
 * Description: For every zombie process created, it displays 'Zombie process created, PID: ZOMBIE_PID'
 *
 * Return: 0 Always
 */

int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		if ((pid = fork()) > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			i++;
		}
		else
			exit (0);
	}

	infinite_while();

	return (0);
}
