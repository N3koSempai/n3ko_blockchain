# Welcome to n3ko blockchain.

[![CodeFactor](https://www.codefactor.io/repository/github/n3kosempai/n3ko_blockchain/badge/master)](https://www.codefactor.io/repository/github/n3kosempai/n3ko_blockchain/overview/master)

I started this blockchain as an exercise for my blockchain development skills.

! Although I do not rule out creating something advanced it is not the goal of this blockchain to go into production !

---

###### warning!

the blockchain is no descentralized yet..

for test the network need to change the ip and port for flask and after run. Use the two endpoint available for mining and get the chain

| features                        | implemented?   |
| ------------------------------- |:--------------:|
| basic structure of a blockchain | yes/~          |
| state of proof design?          | no/but planned |
| mining client                   | no/only inside |
| secure mining algoritm          | no             |
| wallet client                   | no             |
| smart contract support          | no             |

###### endpoints:

```url
http://$IP:$PORT/get_chain
```

this endpoint return the blockchain



```url
http://$IP:$PORT/mine_block
```

this endpoint mine a new block
