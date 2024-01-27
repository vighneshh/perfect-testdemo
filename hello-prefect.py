from prefect import flow, task
from prefect.blocks.system import String
from prefect.filesystems import GitHub

github_block = GitHub.load("github-helloworld")

string_block = String.load("vtest")

@task
def create_msg():
	msg = "From Github: Hello Prefect from task"
	return msg

@flow
def hello_subflow():
	submsg = "Subflow"
	return submsg

@flow
def hello_world():
	submsg = hello_subflow()
	msg = create_msg()
	whole_msg = msg + " , " + submsg + " and " + string_block.value
	print(whole_msg)

if __name__ == "__main__":
	hello_world()
