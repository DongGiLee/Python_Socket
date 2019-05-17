from socket import *
help(socket.bind())
#[AF_INET] AF=adress family; 주소체계 AF_INET = IPv4 AF_INET6 = IPv6
#[SOCK_STREAM] 소켓유형 저것 이외에 SOCK_(DGRAM,RAW,RDM,SEQPACKET)등이있고 SOCK STREAM,SOCK_DGRAM이 보편적
#위 두개는 socket.socket()인자중 family=,type= 의 기본인자값 그래서 이타입의 소켓을 생성하려는경우는 socket.socket() 만사용가능
sk = socket(AF_INET, SOCK_STREAM)

#서버사이드에서만 필요, '' = INADDR_ANY;모든 인터페이스와 연결 '<broadcast>'= INADDR_BROADCAST;
sk.bind(('',8080))

#해당소켓이 몇개의 동시접속을 허용할것인지 인자가없으면 임의의숫자로 listen
#클라이언트가 해당포트에 접속하는것을 기다리고 접속이들어오면 리턴된다.원하는클라이언트인지 임의의 접속요청인지는 알수없다.
sk.listen()

#listen()으로 접속시도를 받고 접속개시를 accept()으로한다.
sk.accept()

connectionSock, addr = sk.accept()