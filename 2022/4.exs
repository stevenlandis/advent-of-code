File.read!("4.txt")
  |> String.split("\n")
  |> Enum.filter(fn line -> line |> String.length > 0 end)
  |> Enum.map(
      fn line -> line
        |> String.split(",")
        |> Enum.map(fn part -> part |> String.split("-") |> Enum.map(fn num -> num |> Integer.parse() |> elem(0) end) end)
        |> then(fn [[a,b], [c,d]] -> (a <= c and d <= b) or (c <= a and b <= d) end)
      end
    )
  |> Enum.filter(fn x -> x end)
  |> length
  |> IO.inspect()

File.read!("4.txt")
  |> String.split("\n")
  |> Enum.filter(fn line -> line |> String.length > 0 end)
  |> Enum.map(
      fn line -> line
        |> String.split(",")
        |> Enum.map(fn part -> part |> String.split("-") |> Enum.map(fn num -> num |> Integer.parse() |> elem(0) end) end)
        |> then(fn [[a,b], [c,d]] -> b >= c and a <= d or a <= d and b >= c end)
      end
    )
    |> Enum.filter(fn x -> x end)
    |> length
    |> IO.inspect()
