import { Ref } from 'vue';
import { ScrollbarInst } from '../../_internal';
import type { MergedTheme } from '../../_mixins';
import type { TimePickerTheme } from '../styles';
export declare type ItemValue = number | 'am' | 'pm';
export interface Item {
    label: string;
    value: ItemValue;
    disabled: boolean;
}
export interface TimePickerInjection {
    mergedThemeRef: Ref<MergedTheme<TimePickerTheme>>;
    mergedClsPrefixRef: Ref<string>;
}
export declare const timePickerInjectionKey: import("vue").InjectionKey<TimePickerInjection>;
export interface PanelRef {
    $el: HTMLElement;
    hourScrollRef?: ScrollbarInst;
    minuteScrollRef?: ScrollbarInst;
    secondScrollRef?: ScrollbarInst;
    amPmScrollRef?: ScrollbarInst;
}
export declare type OnUpdateValue = ((value: number, formattedValue: string) => void) & ((value: number | null, formattedValue: string | null) => void);
export declare type OnUpdateValueImpl = (value: number | null, formattedValue: string | null) => void;
export declare type OnUpdateFormattedValue = ((value: string, timestampValue: number) => void) & ((value: string | null, timestampValue: number | null) => void);
export declare type OnUpdateFormattedValueImpl = (value: string | null, timestampValue: number | null) => void;
export declare type IsHourDisabled = (hour: number) => boolean;
export declare type IsMinuteDisabled = (minute: number, hour: number | null) => boolean;
export declare type IsSecondDisabled = (second: number, minute: number | null, hour: number | null) => boolean;
export declare type Size = 'small' | 'medium' | 'large';
export interface TimePickerInst {
    focus: () => void;
    blur: () => void;
}
