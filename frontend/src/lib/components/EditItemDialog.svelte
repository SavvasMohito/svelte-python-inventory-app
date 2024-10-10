<script lang="ts">
	import { enhance } from '$app/forms';
	import DatePicker from '$lib/components/DatePicker.svelte';
	import { buttonVariants } from '$lib/components/ui/button';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import type { Item } from '$lib/types';
	import { CalendarDate } from '@internationalized/date';
	import Settings2 from 'lucide-svelte/icons/settings-2';

	const { item = $bindable() }: { item: Item } = $props();
	const date = new Date(item.date);
	let calendarDate = new CalendarDate(date.getFullYear(), date.getMonth() + 1, date.getDate());
	let stringDate = $derived(calendarDate.toString());
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline', size: 'icon' })}>
		<Settings2 class="h-5 w-5" />
	</Dialog.Trigger>
	<Dialog.Content class="sm:max-w-xl">
		<Dialog.Header>
			<Dialog.Title>Edit item</Dialog.Title>
			<Dialog.Description
				>Make changes to your item and click save when you're done.</Dialog.Description
			>
		</Dialog.Header>
		<form action="?/updateItem" method="post" class="flex flex-col gap-4" use:enhance>
			<Input id="id" type="hidden" name="id" value={item.id} />
			<div class="grid gap-4 py-4">
				<div class="grid grid-cols-[80px_1fr] items-center gap-4">
					<Label for="name" class="text-right">Name</Label>
					<Input id="name" name="name" value={item.name} required />
				</div>
				<div class="grid grid-cols-[80px_1fr] items-center gap-4">
					<Label for="description" class="text-right">Description</Label>
					<Input id="description" name="description" value={item.description} />
				</div>
				<div class="flex gap-8">
					<div class="grid grid-cols-[80px_1fr] items-center gap-4">
						<Label for="quantity" class="text-right">Quantity</Label>
						<Input id="quantity" name="quantity" value={item.quantity} required />
					</div>
					<div class="grid grid-cols-[auto_1fr] items-center gap-4">
						<Label for="date" class="text-right">Date</Label>
						<Input id="date" type="hidden" name="date" value={stringDate} />
						<DatePicker value={calendarDate} />
					</div>
				</div>
			</div>
			<Button class="self-end" type="submit">Save changes</Button>
		</form>
	</Dialog.Content>
</Dialog.Root>
