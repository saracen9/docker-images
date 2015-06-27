```
root@ba82493811d9:/# netstat -a
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 localhost:8332          *:*                     LISTEN
tcp        0      0 *:8333                  *:*                     LISTEN
tcp        0   1837 ba82493811d9:40620      pool-108-13-16-50.:8333 ESTABLISHED
tcp        0      0 ba82493811d9:42195      ipb219681d.dynamic:8333 ESTABLISHED
tcp6       0      0 localhost:8332          [::]:*                  LISTEN
tcp6       0      0 [::]:8333               [::]:*                  LISTEN
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
```

Therefore the bitcoind server listens, by default, on ports:

|Application|Port|Scope     |
|-----------|----|----------|
|bitcoind   |8332|internal  |
|bitcoind   |8333|external  |
|litecoind  |9332|internal  |
|litecoind  |9333|external  |
