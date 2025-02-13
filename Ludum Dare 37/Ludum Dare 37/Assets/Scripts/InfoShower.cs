using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InfoShower : MonoBehaviour {

	[Multiline]
	public string InfoText = "Test Text!";

	void OnTriggerEnter2D(Collider2D col) {
		Collector collector = col.GetComponent<Collector>();
		if (collector == null || collector.HasCollectible) {
			return;
		}

		Subtitles.ShowText(InfoText);
	}

	void OnTriggerExit2D(Collider2D col) {
		Subtitles.HideText();
	}
}
