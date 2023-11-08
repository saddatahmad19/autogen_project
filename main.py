from autogen import config_list_from_json, AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager


def main():
    config_list = config_list_from_json("CONFIG_LIST")

    llm_config = {"config_list": config_list, "seed": 42}
    user_proxy = UserProxyAgent(
       name="User_proxy",
       system_message="A human admin.",
       code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
       human_input_mode="TERMINATE"
    )
    coder = AssistantAgent(
        name="Coder",
        llm_config=llm_config,
    )
    pm = AssistantAgent(
        name="Product_manager",
        system_message="Creative in software product ideas.",
        llm_config=llm_config,
    )
    groupchat = GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    user_proxy.initiate_chat(manager, problem="Create a blog about AI and Machine Learning, specifically about Large Language Models. Make sure to ask for details about the blog post.")

if __name__ == "__main__":
    main()