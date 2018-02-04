#include <fcntl.h>
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <pthread.h> 
#include <stdlib.h>
void *generate_region_1_1(void * arg) {
  // Open the file and get the file descriptor
  int fd = open((char *) arg, O_RDONLY);
  if (fd < 0) {
    printf("Fail to open the file!");
  }
  int file_size = lseek(fd, 0, SEEK_END);
  int half_size = file_size / 2;
  lseek(fd, 0, SEEK_SET);
  // Create the socket
  int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
  if (socket_fd < 0) {
    printf("Fail to crete the socket!");
  }
  // Set the server address
  struct sockaddr_in server_addr;
  memset(&server_addr, 0, sizeof(struct sockaddr_in));
  server_addr.sin_family = AF_INET;
  if (inet_pton(AF_INET, "127.0.0.1", &(server_addr.sin_addr)) < 0) {
    printf("Fail to execute inet_pton\n");
  }
  uint16_t host_port = 8888;
  uint16_t network_port = htons(host_port);
  server_addr.sin_port = network_port;
  if (connect(socket_fd, (struct sockaddr *) &server_addr, sizeof(struct sockaddr_in)) < 0) {
    printf("Fail to connect\n");
  }
  // Read the file and send out
  wchar_t buff[1024] = {0};
  int result = 0;
  int pointer_position = 0;
  while((result = read(fd, buff, 1024)) > 0) {
    pointer_position = lseek(fd, 0, SEEK_CUR);
    // printf("Current position of the pointer is %d\n", pointer_position);
    if (pointer_position > half_size) {
      int bytes = 1024 - pointer_position + half_size;
      if (write(socket_fd, buff, bytes) < 0) {
        printf("Fail to write\n");
      }
      break;
    }
    if (write(socket_fd, buff, 1024) < 0) {
      printf("Fail to write\n");
    }
  }
  
}
void *generate_region_1_2(void * arg) {
  // Open the file and get the file descriptor
  int fd = open((char *) arg, O_RDONLY);
  if (fd < 0) {
    printf("There is something wrong when reading the file.");
  }
  // Calculate the file size
  int file_size = lseek(fd, 0, SEEK_END);
  int half_size = file_size / 2;
  lseek(fd, half_size, SEEK_SET);
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
  // printf("Current position: %d\n", lseek(fd, 0, SEEK_CUR));
  while((read_result = read(fd, buf, 1024)) > 0) {
    if (write(socket_fd, buf, 1024) < 0) {
      printf("Failt to write!\n");
    }
  }
}

int main(int argc, char* argv[]) {
  char* file_name;
  int file_number = argc - 1;
  pthread_t thread_1[file_number];
  pthread_t thread_2[file_number];
  for (int i = 0; i < file_number; i++) {
    file_name = argv[i + 1];
    int result_1 = pthread_create(&thread_1[i], NULL, generate_region_1_1, file_name);
    if (result_1 != 0) {
      printf("Fail to create the thread_0\n");
    }
    int result_2 = pthread_create(&thread_2[i], NULL, generate_region_1_2, file_name);
    if (result_2 != 0) {
      printf("Fail to create the thread_2\n");
    }
  }
  for (int i = 0; i < file_number; i++) {
    pthread_join(thread_1[i], NULL);
    pthread_join(thread_2[i], NULL);
  }
}
