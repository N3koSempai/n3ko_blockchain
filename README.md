# Welcome to n3ko blockchain.

[![CodeFactor](https://www.codefactor.io/repository/github/n3kosempai/n3ko_blockchain/badge/master)](https://www.codefactor.io/repository/github/n3kosempai/n3ko_blockchain/overview/master)

I started this blockchain as an exercise for my blockchain development skills.

! Although I do not rule out creating something advanced it is not the goal of this blockchain go into production !

---

###### warning!

the blockchain is no descentralized yet..

for test the network need to change the ip and port for flask and after run. Use the two endpoint available for mining and get the chain

| features                        | implemented?     |
| ------------------------------- |:----------------:|
| basic structure of a blockchain | yes/~            |
| node sync                       | yes/ manual sync |
| state of proof design?          | no/but planned   |
| mining client                   | no/only inside   |
| secure mining algoritm          | no               |
| wallet client                   | no               |
| smart contract support          | no               |

###### endpoints:

This endpoint return the blockchain:

```url
GET
http://$IP:$PORT/get_chain
```

This endpoint mine a new block:

```url
GET
http://$IP:$PORT/mine_block
```

This endpoint add new nodes (need json body with the nodes):

the new nodes need to be started and listen in the ip and port selected

```url
POST
http://$IP:$PORT/connect_node
```

```json
{"nodes" : ["http://$IP:$PORT", "http: another IP and port", "...."]}
```

This endpoint syncronizes the nodes (manual for now):

```url
GET
http://$IP:$PORT/replace_chain
```

This endpoint add transaction (for added to the blockchain you need mine block after):

```url
POST
http://$IP:$PORT/add_trans
```

added the transaction detail in the json body of the petition

```json
{
    "sender": "any",
    "receiver": "any",
    "amount": 100
}
```
