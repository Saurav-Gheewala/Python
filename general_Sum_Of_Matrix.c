#include <stdio.h>
#include <conio.h>
void main()
{
int i,j,r,c;
printf("Enter The Value Of Row");    
scanf("%d", &r);
printf("Enter The Value Of Colum");  
scanf("%d", &c);
int a[r][c],b[r][c],s[r][c];
printf("Enter value:\n ");
for(i=0; i<r ; i++)
{
        for(j=0; j<c ; j++)
    {
        scanf("%d", &a[i][j]);
    }
}
printf("\n The Matrix is ::: \n" );
for(i=0; i<r ; i++)
{
        for(j=0; j<c ; j++)
    {
        printf("%d  ", a[i][j]);
    }    
        printf("\n");
}
printf("Enter value:\n ");
for(i=0; i<r ; i++)
{
        for(j=0; j<c ; j++)
    {
        scanf("%d", &b[i][j]);
    }
}
printf("\n The Matrix is ::: \n" );
for(i=0; i<r ; i++)
{
        for(j=0; j<c ; j++)
    {
        printf("%d  ", b[i][j]);
    }    
        printf("\n");
}        
        printf("\n The Sum Of Matrix is ::: \n" );
for(i=0; i<r ; i++)
{
        for(j=0; j<c ; j++)
    {
        s[i][j]=a[i][j]+b[i][j];
        printf("%d  ", s[i][j]);
    }    
        printf("\n");
}

}