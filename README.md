# fil plus checker
Fil plus checker is a tool for retrieval data based on deal it.The retrieval logs will be stored at logs/<deal_id>.log

## How to use

```commandline
chmod 700 lite_node.sh
./lite_node.sh
```

In another terminal,
```shell
python main.py <deal_id>
```

check the log for progress

```shell
tail -f log/<deal_id>.log
```
