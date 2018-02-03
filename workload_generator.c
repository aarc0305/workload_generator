#include <fcntl.h>
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <pthread.h> 
#include <stdlib.h>

void *generate_region_1(void * arg) {
  // Open the file and get the file descriptor
  int fd = open("./vehicle_data_region_1", O_RDONLY);
  if (fd < 0) {
    printf("There is something wrong when reading the file.");
  }
  // Use lseek to get the file size
  int file_size = lseek(fd, 0, SEEK_END);
  printf("The size of the file is %d\n", file_size);
  printf("The half of the file size is %d\n", file_size / 2);
  // Move the pointer back to the starting point of the file
  printf("The offset is %d\n", *((int *) arg));
  lseek(fd, 0, SEEK_SET);
  // Create the socket
  int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
  if (socket_fd < 0) {
    printf("Fail to create the socket!\n");
  }
  // Set the server address and port
  struct sockaddr_in server_addr;
  memset(&server_addr, 0, sizeof(struct sockaddr_in));
  server_addr.sin_family = AF_INET;
  if (inet_pton(AF_INET, "127.0.0.1", &(server_addr.sin_addr)) < 0) {
    printf("Fail to execute inet_pton\n");
  }
  uint16_t host_port = 8888;
  uint16_t network_port = htons(host_port);
  server_addr.sin_port = network_port;
  if (connect(socket_fd, (struct sockaddr*) &server_addr, sizeof(struct sockaddr_in)) < 0) {
    printf("Fail to connect!\n");
  }
  // Read the file and send out
  wchar_t buf[1024] = {0};
  int read_result = 0;
  while((read_result = read(fd, buf, 1024)) > 0) {
    // printf("%s\n", buf);
    if (write(socket_fd, buf, 1024) < 0) {
      printf("Failt to write!\n");
    }
  }
}

int main(int argc, char* argv[]) {
  pthread_t thread_0;
  pthread_t thread_1;
  int offset_0 = 0;
  int offset_1 = 1;
  int result_0 = pthread_create(&thread_0, NULL, generate_region_1, &offset_0);
  if (result_0 != 0) {
    printf("Fail to create the thread_0\n");
  }
  int result_1 = pthread_create(&thread_1, NULL, generate_region_1, &offset_1);
  if (result_1 != 0) {
    printf("Fail to create the thread_!\n");
  }
  pthread_join(thread_0, NULL);
  pthread_join(thread_1, NULL);

}
