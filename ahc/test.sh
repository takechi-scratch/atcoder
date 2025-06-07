rm answer/*
rm message.txt

trap 'echo "\n中断されました"; exit 130' INT

for f in tests/*.in; do
  filename=$(basename "$f" .in)
  # 標準エラー出力をリアルタイムでコンソールに出しつつ、message.txtにも追記
  python main.py < "$f" > "answer/${filename}.out" 2> >(tee -a message.txt >&2)
done

trap - INT

grep 'Score:' message.txt | sed -E 's/.*Score: *([0-9]+).*/\1/' | awk '{sum+=$1} END{print sum}'
