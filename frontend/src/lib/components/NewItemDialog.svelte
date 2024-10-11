<script lang="ts">
	import { enhance } from '$app/forms';
	import DatePicker from '$lib/components/DatePicker.svelte';
	import * as Alert from '$lib/components/ui/alert/index.js';
	import { buttonVariants } from '$lib/components/ui/button';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import { CalendarDate } from '@internationalized/date';
	import Plus from 'lucide-svelte/icons/plus';

	import type { ActionData } from '../../routes/$types';

	let form: ActionData = $state(null);
	let open = $state(false);
	let loading = $state(false);

	const today = new Date();
	let name = '';
	let description = '';
	let quantity = '';
	let calendarDate = $state(
		new CalendarDate(today.getFullYear(), today.getMonth() + 1, today.getDate())
	);
	let stringDate = $derived(calendarDate.toString());
</script>

<Dialog.Root bind:open>
	<Dialog.Trigger class={buttonVariants()}><Plus class="mr-1 h-5 w-5" />Add new item</Dialog.Trigger
	>
	<Dialog.Content class="sm:max-w-xl">
		<Dialog.Header>
			<Dialog.Title>Add new item</Dialog.Title>
			<Dialog.Description>
				Add the details of your item and submit them when you're done.
			</Dialog.Description>
		</Dialog.Header>
		<form
			action="?/createItem"
			method="post"
			class="flex flex-col gap-4"
			use:enhance={() => {
				loading = true;
				return async ({ result, update }) => {
					loading = false;
					if (result.type === 'success') {
						open = false;
						update({ invalidateAll: true });
					} else if (result.type === 'failure') {
						form = { error: result.data?.error };
					}
				};
			}}
		>
			<div class="grid gap-4 py-4">
				<div class="grid grid-cols-[80px_1fr] items-center gap-4">
					<Label for="name" class="text-right">Name</Label>
					<Input id="name" name="name" value={name} placeholder="Item name" required />
				</div>
				<div class="grid grid-cols-[80px_1fr] items-center gap-4">
					<Label for="description" class="text-right">Description</Label>
					<Input
						id="description"
						name="description"
						value={description}
						placeholder="Item description"
					/>
				</div>
				<div class="flex gap-8">
					<div class="grid grid-cols-[80px_1fr] items-center gap-4">
						<Label for="quantity" class="text-right">Quantity</Label>
						<Input
							id="quantity"
							name="quantity"
							value={quantity}
							placeholder="Item quantity"
							required
						/>
					</div>
					<div class="grid grid-cols-[auto_1fr] items-center gap-4">
						<Label for="date" class="text-right">Date</Label>
						<Input id="date" type="hidden" name="date" value={stringDate} />
						<DatePicker bind:value={calendarDate} />
					</div>
				</div>
			</div>
			<Button disabled={loading} class="self-end" type="submit">Add to inventory</Button>
			{#if form?.error}
				<Alert.Root variant="destructive" class="text-center font-semibold">
					<Alert.Description>{form?.error}</Alert.Description>
				</Alert.Root>
			{/if}
		</form>
	</Dialog.Content>
</Dialog.Root>
