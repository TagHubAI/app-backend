export declare type OnUpdateValue = ((value: string[]) => void) | ((value: DynamicTagsOption[]) => void);
export declare type OnUpdateValueImpl = (value: Array<string | DynamicTagsOption>) => void;
export declare type OnCreate = (label: string) => {
    label: string;
    value: string;
} | string;
export interface DynamicTagsOption {
    label: string;
    value: string;
}
