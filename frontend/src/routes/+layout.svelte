<script>
	import '../app.css';

	let { children } = $props();
</script>

<div class="flex h-screen flex-col p-10">
	{@render children()}
	<div class="absolute bottom-2 self-center text-sm text-gray-500">
		Developed by <a
			class="text-primary hover:underline"
			href="https://github.com/SavvasMohito"
			target="_blank">Savvas Mantzouranidis</a
		>
		for the first assignment of PA2577
	</div>
</div>
