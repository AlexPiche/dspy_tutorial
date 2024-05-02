import dspy


def test_setup():
    lm = dspy.HFClientVLLM(
        model="meta-llama/Meta-Llama-3-8B", port=8080, url="http://localhost"
    )
    dspy.settings.configure(lm=lm)
    out = dspy.Predict("question -> answer", max_tokens=1)(question="what is the capital of france?")
    assert out.answer.lower() == "paris"
    print("setup works!")
    
    
    
if __name__ == "__main__":
    test_setup()
