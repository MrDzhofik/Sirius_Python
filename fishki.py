def clean(N):
  if N <= 2:
      return list(range(-N, 0))
  return clean(N - 2) + [-N] + fill(N - 2) + clean(N - 1)
 
 
def fill(N):
  if N <= 2:
      return list(range(1, N + 1))
  return fill(N - 1) + clean(N - 2) + [N] + fill(N - 2)
 
print(*fill(int(input())))