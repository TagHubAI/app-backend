import { VNodeChild } from 'vue';
import type { MessageSetupProps } from './message-props';
export declare type MessageType = 'info' | 'success' | 'warning' | 'error' | 'loading' | 'default';
export declare type RenderMessageProps = Pick<MessageSetupProps, 'closable' | 'content' | 'icon' | 'onClose' | 'type'>;
export declare type MessageRenderMessage = (props: RenderMessageProps) => VNodeChild;
export interface MessageOptions {
    type?: MessageType;
    render?: MessageRenderMessage;
    duration?: number;
    closable?: boolean;
    keepAliveOnHover?: boolean;
    icon?: () => VNodeChild;
    showIcon?: boolean;
    onClose?: () => void;
    onLeave?: () => void;
    onAfterLeave?: () => void;
}
