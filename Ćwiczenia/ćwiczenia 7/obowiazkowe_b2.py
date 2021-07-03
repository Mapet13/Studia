
def zad(S, P, L):
	F = [-1]*len(S)	
	def f(m):
		if m == 0:
			return 0
		mini = float('inf')
		j = m-1
		while j >= 0 and S[m]-S[j]<=L:
			if F[j] == -1:
				F[j] = f(j)
			val = F[j]+(S[m]-S[j])*P[j]
			mini = min(mini, val)
			j-=1
		return mini

	ans = f(len(S)-1)
	return ans

print(zad(S,P,L))
