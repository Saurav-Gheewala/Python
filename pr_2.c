#include<stdio.h>
#include<conio.h>
void main()
{
    int n1,n2,n3;
    printf("Enter The All Three Number.\n");
    printf("Enter The Frist Number.\n");
    scanf("%d", &n1);
    printf("Enter The Second Number.\n");
    scanf("%d", &n2);
    printf("Enter The Third Number.\n");
    scanf("%d", &n3);
    if (n1>n2)
        {
            if (n1>n3)
                {    
                    printf("The Greatest Number Is Frist Number.\n");
                }
            else
                {
                    printf("The Greatest Nmuber Is Third Number\n"); 
                }
        }
    else
        {
            if (n2>n3)
                {
                    printf("The Greatest Number Is Second Number.\n");
                }
            else
                {
                    printf("The Greatest Number Is Third Number.\n");
                }    
        }

}