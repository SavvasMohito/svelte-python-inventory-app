<script lang="ts">
	import { enhance } from '$app/forms';
	import DatePicker from '$lib/components/DatePicker.svelte';
	import { buttonVariants } from '$lib/components/ui/button';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import { CalendarDate } from '@internationalized/date';

	const today = new Date();
	let name = '';
	let description = '';
	let quantity = '';
	let calendarDate = $state(
		new CalendarDate(today.getFullYear(), today.getMonth() + 1, today.getDate())
	);
	let stringDate = $derived(calendarDate.toString());
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants()}>+ Add new item</Dialog.Trigger>
	<Dialog.Content class="sm:max-w-xl">
		<Dialog.Header>
			<Dialog.Title>Add new item</Dialog.Title>
			<Dialog.Description>
				Add the details of your item and submit them when you're done.
			</Dialog.Description>
		</Dialog.Header>
		<form action="?/createItem" method="post" class="flex flex-col gap-4" use:enhance>
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
			<Button class="self-end" type="submit">Add to inventory</Button>
		</form>
	</Dialog.Content>
</Dialog.Root>
