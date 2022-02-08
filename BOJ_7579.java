package algorithm_2022;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_7579 {

	public static void main(String[] args) throws IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int arr[] = new int[N];
		int cost[] = new int[N];
		st = new StringTokenizer(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {arr[i] = Integer.parseInt(st.nextToken());
		cost[i] = Integer.parseInt(st2.nextToken());}
		
		ArrayList<int []> al = new ArrayList<>();
		
		for(int i=0;i<N;i++) {
			int sum =arr[i];
			int csum =cost[i];
			for(int j=i;j<N;j++) {
				if(i!=j) {
					// 첫번째는 byte 두번째는 cost
					sum += arr[j];
					csum+= cost[j];
				}
				al.add(new int[] {sum, csum});
			}
		}
		int answer = Integer.MAX_VALUE;
		for(int i=0;i<al.size();i++) {
			int c = al.get(i)[1];
			int b = al.get(i)[0];
			if(b>=M) {
				answer = answer > c ? c : answer;
			}
		}
		System.out.println(answer);
	}
}
