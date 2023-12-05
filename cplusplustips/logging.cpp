// use assert() 
/*  
* memcpy()는 pvSource 로부터 pvSink 로 sz 만큼을 복사함. 
* memcpy()는 pvSource 와 pvSink 가 NULL 이 아니라는 걸 가정하고 있음 
*/
#include "stdio.h"
void* memcpy(void* pvSink, void* pvSource, size_t sz)
{ 
    char* pSrc = (char*)pvSource;
    char* pSnk = (char*)pvSink;
    #ifdef DEBUG // production 레벨에서는 NULL이 나와도 강제로 abort되는 경우가 생기면 사용자들에게 올바른 서비스를 제공할 수 없다. 따라서 DEBUG 일때만 체크
    // 만약 pvSource 나 pvSink가 NULL이면 프로그램 중단
    if (pvSource == NULL || pvSink == NULL)
    {
        fprintf(stderr, "memcpy(): Bad args: pvSource or pvSink is NULL\n");
        abort();
    }
    #endif
    while (sz-- > 0)
        *pSnk++ = *pSrc++; 
    return pvSink;
}
