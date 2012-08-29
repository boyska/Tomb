#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/time.h>

#include <openssl/x509.h>
#include <openssl/evp.h>
#include <openssl/hmac.h>

static long bench(int ic) {
	char *pass = "mypass";
	unsigned char *salt = "abcdefghijklmno";
	int salt_len = strlen(salt);
	int result_len = 64;
	unsigned char *result = calloc(result_len, sizeof(char));
	struct timeval start, end;
	long microtime;

	gettimeofday(&start, NULL);
	PKCS5_PBKDF2_HMAC_SHA1(pass, strlen(pass), salt, salt_len, ic, result_len, result);
	gettimeofday(&end, NULL);
	microtime = 1000000*end.tv_sec+end.tv_usec - (1000000*start.tv_sec+start.tv_usec);

	return (long)microtime;
}
int main(int argc, char *argv[])
{
	long desired_time = 1000000;
	long microtime;
	int ic=100;
	int tries=0;
	if(argc >= 2)
		sscanf(argv[1], "%ld", &desired_time);

	microtime = bench(ic);
	while( abs(desired_time-microtime) > (desired_time/10) /*little difference */ 
			&& tries++ <= 5) {
		float ratio = (float)desired_time/microtime;
		if(ratio > 1000) ratio=1000.0;
		ic*=ratio;
		if(ic<1) ic=1;
		microtime = bench(ic);
	} 
	printf("%d\n", ic);
	return 0;

}
