// *                     * 
// * *                 * *
// * * *             * * *
// * * * *         * * * *
// * * * * *     * * * * *
// * * * * * * * * * * * *
// * * * * *     * * * * * 
// * * * *         * * * * 
// * * *             * * * 
// * *                 * *
// *                     *

#include<iostream>
using namespace std;
 
int main()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j <=i; j++)
        {
            cout<<"* ";
        }
        for (int k = 0; k <5-i; k++)
        {
            cout<<"    ";
        }
        for (int l = 0; l <=i; l++)
        {
            cout<<"* ";
        }
        
        cout<<endl;
        
    }
      for (int i = 5; i >=0; i--)
    {
        for (int j = 0; j <=i; j++)
        {
            cout<<"* ";
        }
        for (int k = 0; k <5-i; k++)
        {
            cout<<"    ";
        }
        for (int l = 0; l <=i; l++)
        {
            cout<<"* ";
        }
        
        cout<<endl;
        
    }
    
    return 0;
}