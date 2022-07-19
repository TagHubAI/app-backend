import type { SelectBaseOption } from '../../select/src/interface';
export declare type MentionOption = SelectBaseOption<string>;
export interface MentionInst {
    focus: () => void;
    blur: () => void;
}
