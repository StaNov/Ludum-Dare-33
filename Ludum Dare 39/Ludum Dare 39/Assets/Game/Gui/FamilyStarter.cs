using GameOfLife.GameLogic;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FamilyStarter : MonoBehaviour
{
	public GameObject[] FamilyObjects;
	public GameStateHolder State;

	private void Start()
	{
		foreach (var familyObject in FamilyObjects)
		{
			familyObject.SetActive(false);
		}
	}

	public void StartFamily ()
	{
		foreach (var familyObject in FamilyObjects)
		{
			familyObject.SetActive(true);
		}

		gameObject.SetActive(false);
		State.State.StartFamily();
	}
}
