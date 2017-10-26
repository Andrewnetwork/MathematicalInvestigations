void HeftyCounter::incrementCounter( unsigned long int quantity)
{
	if(  quantity  != 0 )
	{
		unsigned long int        remainder         = quantity;
		unsigned long long int   additionRemainder = 0;
		unsigned int             counterIndex      = 0;
		unsigned                 additionTemp      = 0;
		int                      digitCount        = 1;


		// Convert quantity to the counters base and add it to the counter at the same time.
		do
		{
			counterIndex = this->counterSize - digitCount;

			additionTemp = ( counter[ counterIndex  ] + (remainder % base ) + additionRemainder);

			counter[ counterIndex ] = additionTemp % base;

			additionRemainder = additionTemp / base;

			remainder = remainder / base;

			if( (additionRemainder > 0 || remainder > 0) && digitCount >= this->counterSize )
			{
				// Overflow.
				counter.insert( counter.begin(), 0 );
				++this->counterSize;
			}

			digitCount++;

		}while( remainder > 0  || additionRemainder > 0  );

	}
}
