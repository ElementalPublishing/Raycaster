from raycaster.core.events import Event, EventDispatcher


def test_event_creation():
    e = Event("test_event", {"foo": 123})
    assert e.name == "test_event"
    assert e.data["foo"] == 123


def test_register_and_dispatch():
    dispatcher = EventDispatcher()
    called = {}

    def listener(event):
        called["event"] = event

    dispatcher.register("my_event", listener)
    count = dispatcher.dispatch("my_event", {"bar": 456})
    assert "event" in called
    assert called["event"].name == "my_event"
    assert called["event"].data["bar"] == 456
    assert count == 1


def test_unregister():
    dispatcher = EventDispatcher()
    called = {}

    def listener(event):
        called["event"] = True

    dispatcher.register("evt", listener)
    dispatcher.unregister("evt", listener)
    dispatcher.dispatch("evt")
    assert "event" not in called


def test_clear():
    dispatcher = EventDispatcher()
    called = {}

    def listener(event):
        called["event"] = True

    dispatcher.register("evt", listener)
    dispatcher.clear()
    dispatcher.dispatch("evt")
    assert "event" not in called


def test_multiple_listeners():
    dispatcher = EventDispatcher()
    calls = []

    def l1(event):
        calls.append("l1")

    def l2(event):
        calls.append("l2")

    dispatcher.register("evt", l1)
    dispatcher.register("evt", l2)
    count = dispatcher.dispatch("evt")
    assert "l1" in calls and "l2" in calls
    assert count == 2


def test_listener_exception_does_not_break_dispatch(capsys):
    dispatcher = EventDispatcher()
    calls = []

    def bad_listener(event):
        raise ValueError("fail")

    def good_listener(event):
        calls.append("good")

    dispatcher.register("evt", bad_listener)
    dispatcher.register("evt", good_listener)
    count = dispatcher.dispatch("evt")
    assert "good" in calls
    assert count == 2
    out = capsys.readouterr().out
    assert "Error in listener" in out
