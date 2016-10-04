#include <iostream>

using namespace std;

void simplenums(int num)
{
	int k;
	for (int i = 2 ; i <= num ; ++i)
	{
		for (int j = 2 ; j < i ; ++j )
		{
			if (!(i%j))
				k++;
		}
		if (k)
			k = 0;
		else
			cout<<i<<endl;
	}
}
void one_more_simple(int num)
{
	simplenums(num);
	int k = 0;
	while (1)
	{
		for (int j = 2 ; j < num ; ++j )
		{
			if (!(num%j))
				k++;
		}
		if (k)
		{
			k = 0;
			num++;
		}
		else
		{
			cout<<num<<endl;	
			break;
		}
	}
}

int main(int argc, char const *argv[])
{
	int num;
	cin >> num;
	one_more_simple(num);
	return 0;
}