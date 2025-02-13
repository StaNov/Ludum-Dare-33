using GameOfLife.GameLogic.GameStateAction;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class StatsAffector : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
	public GameplayConstants Constants;
	public HoveredActionEffect Effect;

	private Dictionary<string, StateAction> _actions;

	private void Start()
	{
        _actions = new Dictionary<string, StateAction>();

        foreach (var action in Constants.GetPlayerActions())
            _actions.Add(action.GetName(), action);
	}

	public void OnPointerEnter(PointerEventData eventData)
	{
		var playerAction = _actions[gameObject.name];
		Effect.SetEffect(playerAction);
	}

	public void OnPointerExit(PointerEventData eventData)
	{
		Effect.ResetDifference();
	}
}
