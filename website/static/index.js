function deletetask(taskId) {
  fetch("/deletetask", {
    method: "POST",
    body: JSON.stringify({taskId: taskId}),
  }).then((_res) => {window.location.href = "/todo";});
}