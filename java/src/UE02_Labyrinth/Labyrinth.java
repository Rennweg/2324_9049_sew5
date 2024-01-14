
//TODO: Mein Name in der Javadoc

import java.util.HashSet;
import java.util.Set;

public class Labyrinth {
	public static String[][] maps = {{
		"############",
		"#  #     # #",
		"## # ### # #",
		"#  # # # # #",
		"## ### # # #",
		"#        # #",
		"## ####### #",
		"#          #",
		"# ######## #",
		"# #   #    #",
		"#   #   # ##",
		"######A#####"
	}, {
		"################################",
		"#                              #",
		"# ############################ #",
		"# # ###       ##  #          # #",
		"# #     ##### ### # ########## #",
		"# #   ##### #     # #      ### #",
		"# # ##### #   ###   # # ## # # #",
		"# # ### # ## ######## # ##   # #",
		"# ##### #  # #   #    #    ### #",
		"# # ### ## # # # # ####### # # #",
		"# #        # #   #     #     # #",
		"# ######## # ######### # ### # #",
		"# ####     #  # #   #  # ##### #",
		"# # #### #### # # # # ## # ### #",
		"#                      # #     #",
		"###########################A####"
	}, {
		"###########################A####",
		"#   #      ## # # ###  #     # #",
		"# ###### #### # # #### ##### # #",
		"# # ###  ## # # # #          # #",
		"# # ### ### # # # # # #### # # #",
		"# #     ### # # # # # ## # # # #",
		"# # # # ### # # # # ######## # #",
		"# # # #     #          #     # #",
		"# ### ################ # # # # #",
		"# #   #             ## # #   # #",
		"# # #### ############# # #   # #",
		"# #                    #     # #",
		"# # #################### # # # #",
		"# # #### #           ###     # #",
		"# # ## # ### ### ### ### # ### #",
		"# #    #     ##  ##  # ###   # #",
		"# ####   ###### #### # ###  ## #",
		"###########################A####"
	}, {
		"#############",
		"#           #",
		"#           #",
		"#           #",
		"###########A#"
	}};

	/**
	 * Wandelt (unveränderliche) Strings in Char-Arrays
	 * @param map  der Plan, ein String je Zeile
	 * @return char[][] des Plans
	 */
	public static char[][] fromStrings(String[] map) {
        char[][] res = new char[map.length][map[0].length()];
		for (int i = 0; i < map.length; i++) {
			String st = map[i];
			char[] s = st.toCharArray();
			for (int j = 0; j < s.length; j++) {
				res[i][j] = s[j];
			}

		}

		return res;
	}


	/**
	 * Ausgabe des Layrinths
	 * @param lab
	 */
	public static void printLabyrinth(char[][] lab) {
		for (int i = 0; i < lab.length; i++) {
			for (int j = 0; j < lab[0].length; j++) {
				System.out.print(lab[i][j]);
			}
			System.out.println();
		}
	}

	/**
	 * Suche den Weg
	 * @param zeile     aktuelle Position
	 * @param spalte     aktuelle Position
	 * @param lab
	 * @throws InterruptedException    für die verlangsamte Ausgabe mit sleep()
	 */
	public static boolean suchen(int zeile, int spalte, char[][] lab) throws InterruptedException {
		if (lab[zeile][spalte] == 'A'){
			return true;
		} else if (lab[zeile][spalte]=='#') {
			return false;
		} else if (lab[zeile][spalte]=='O') {
			return false;
		}else {
			lab[zeile][spalte] = 'O';
		}
//		printLabyrinth(lab);
		if (suchen(zeile, spalte+1, lab) || suchen(zeile, spalte-1, lab) || suchen(zeile+1, spalte, lab) || suchen(zeile-1, spalte, lab)){
			return true;
		}

		return false;
	}

	public static int suchenAlle(int zeile, int spalte, char[][] lab, Set visited, int count) throws InterruptedException {
		if (lab[zeile][spalte] == 'A'){
			return 1;
		} else if (lab[zeile][spalte]=='#') {
			return 0;
		}
		int len = visited.size();
		visited.add(Integer.toString(zeile)+ "_"+Integer.toString(spalte));
		if (len == visited.size()) {
			return 0;
		}

		count += suchenAlle(zeile, spalte+1, lab, visited, count);
		count += suchenAlle(zeile, spalte-1, lab, visited, count);
		count += suchenAlle(zeile+1, spalte, lab, visited, count);
		count += suchenAlle(zeile-1, spalte, lab, visited, count);

		return count;
	}

	public static void main(String[] args) throws InterruptedException {
		char[][] labyrinth = fromStrings(maps[0]);
		printLabyrinth(labyrinth);
		System.out.println("Ausgang gefunden: " + (suchen(5, 5, labyrinth) ? "ja" : "nein"));
		Set visited = new HashSet();
		System.out.println("Anzahl Wege: " + suchenAlle(5, 5, labyrinth, visited, 0));
	}
}
