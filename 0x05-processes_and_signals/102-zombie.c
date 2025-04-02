#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to keep the program running
 *
 * Return: Always returns 0
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
 * main - Creates 5 zombie processes
 *
 * Return: Always returns 0
 */
int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0)
        {
            /* Child process exits immediately to become a zombie */
            exit(0);
        }
        else
        {
            /* Parent process prints message with zombie PID */
            printf("Zombie process created, PID: %d\n", pid);
        }
    }

    /* Keep parent process running */
    infinite_while();

    return (0);
} 