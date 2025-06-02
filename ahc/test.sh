for f in tests/*.in; do
  filename=$(basename "$f" .in)
  python main.py < "$f" > "answer/${filename}.out"
done
