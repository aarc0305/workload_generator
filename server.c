#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define BACKLOG 10
int main(int argc, char* argv[]) {
  int fd = socket(AF_INET, SOCK_STREAM, 0);
  if( fd < 0) {
    printf("There are something wrong when creating socket\n");
  }
  printf("The fd of the socket is %d\n", fd);
  // Set the ipv4 address
  struct sockaddr_in saddr;
  memset(&saddr, 0, sizeof(struct sockaddr_in));
  saddr.sin_family = AF_INET;
  if (inet_pton(AF_INET, "127.0.0.1", &(saddr.sin_addr)) < 0) {
    printf("inet_pton failed!\n");
  }
  printf("saddr.sin_addr.s_addr: %d\n", saddr.sin_addr.s_addr);
  uint16_t host_port = 8888;
  uint16_t network_port = htons(host_port);
  saddr.sin_port = network_port;
  printf("saddr.sin_port: %d\n", saddr.sin_port);
  if (bind(fd, (struct sockaddr*) &saddr, sizeof(struct sockaddr_in)) == -1) {
    printf("Fail to bind the address!\n");
  }
  if (listen(fd, BACKLOG) < 0) {
    printf("Fail to listen.\n");
  }
  for(;;) {
    wchar_t buff[1024] = {0};
    int cfd = accept(fd, NULL, NULL);
    printf("There is one client: %d\n", cfd);    
    while(recvfrom(cfd, buff, 1024, 0, NULL, NULL) > 0) {
      printf("%s\n", buff);
    }
  }  
}
