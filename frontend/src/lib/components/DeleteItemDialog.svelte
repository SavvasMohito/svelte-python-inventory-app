<script lang="ts">
	import { enhance } from '$app/forms';
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { Button } from '$lib/components/ui/button';
	import type { Item } from '$lib/types';
	import { Trash2 } from 'lucide-svelte';

	const { item = $bindable() }: { item: Item } = $props();
</script>

<AlertDialog.Root>
	<AlertDialog.Trigger asChild let:builder>
		<Button builders={[builder]} size="icon">
			<Trash2 class="h-5 w-5" />
		</Button>
	</AlertDialog.Trigger>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Are you sure you want to delete {item.name}?</AlertDialog.Title>
			<AlertDialog.Description>This action cannot be undone.</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<form action="?/deleteItem" method="post" use:enhance>
				<input type="hidden" name="id" value={item.id} />
				<AlertDialog.Action type="submit">Delete</AlertDialog.Action>
			</form>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
