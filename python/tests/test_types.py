import os
import tempfile
import unittest
from pathlib import Path

from mypy import api

import crawlora_sofascore as client_package


TYPECHECK_SOURCE = '''
from typing_extensions import assert_type
from crawlora_sofascore import AsyncClient, AsyncSofascoreClient, Client, SofascoreClient
from crawlora_sofascore.platform import SofascoreTournamentTopTeamsResponse

def check_sync() -> None:
    named: SofascoreClient = Client(api_key="key")
    with Client(api_key="key") as client:
        assert_type(client.tournament_top_teams(id='test value', season='test value', type='overall'), SofascoreTournamentTopTeamsResponse)
        assert_type(client.tournament_top_teams(_response_type='text', id='test value', season='test value', type='overall'), str)
        assert_type(client.tournament_top_teams(_response_type='stream', id='test value', season='test value', type='overall').read(), bytes)
        assert_type(client.request('sofascore-tournament-top-teams', {'id': 'test value', 'season': 'test value', 'type': 'overall'}), SofascoreTournamentTopTeamsResponse)
        assert_type(client.sofascore.tournament_top_teams(id='test value', season='test value', type='overall'), SofascoreTournamentTopTeamsResponse)
        assert_type(client.sofascore.tournament_top_teams(_response_type='text', id='test value', season='test value', type='overall'), str)
        assert_type(client.sofascore.tournament_top_teams(_response_type='stream', id='test value', season='test value', type='overall').read(), bytes)



async def check_async() -> None:
    named: AsyncSofascoreClient = AsyncClient(api_key="key")
    async with AsyncClient(api_key="key") as client:
        assert_type(await client.tournament_top_teams(id='test value', season='test value', type='overall'), SofascoreTournamentTopTeamsResponse)
        assert_type(await client.tournament_top_teams(_response_type='text', id='test value', season='test value', type='overall'), str)
        assert_type((await client.tournament_top_teams(_response_type='stream', id='test value', season='test value', type='overall')).read(), bytes)
        assert_type(await client.sofascore.tournament_top_teams(id='test value', season='test value', type='overall'), SofascoreTournamentTopTeamsResponse)
        assert_type(await client.sofascore.tournament_top_teams(_response_type='text', id='test value', season='test value', type='overall'), str)
        assert_type((await client.sofascore.tournament_top_teams(_response_type='stream', id='test value', season='test value', type='overall')).read(), bytes)


'''

NEGATIVE_SOURCE = '''
from crawlora_sofascore import Client
Client().tournament_top_teams(id=123, season='test value', type='overall')
Client().tournament_top_teams()
'''


class PublicTypingTests(unittest.TestCase):
    def setUp(self):
        self.package_root = Path(client_package.__file__).resolve().parent
        self.old_mypy_path = os.environ.get("MYPYPATH")
        parent = str(self.package_root.parent)
        os.environ["MYPYPATH"] = parent if self.old_mypy_path is None else parent + os.pathsep + self.old_mypy_path

    def tearDown(self):
        if self.old_mypy_path is None:
            os.environ.pop("MYPYPATH", None)
        else:
            os.environ["MYPYPATH"] = self.old_mypy_path

    def test_installed_platform_stub_is_well_formed(self):
        stdout, stderr, status = api.run([
            "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent",
            str(self.package_root / "platform.pyi"),
        ])
        self.assertEqual(status, 0, stdout + stderr)

    def test_installed_client_signatures_accept_valid_calls_and_reject_invalid_calls(self):
        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-") as temp:
            source_path = Path(temp) / "typecheck.py"
            source_path.write_text(TYPECHECK_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertEqual(status, 0, stdout + stderr)

        with tempfile.TemporaryDirectory(prefix="crawlora-python-mypy-negative-") as temp:
            source_path = Path(temp) / "invalid.py"
            source_path.write_text(NEGATIVE_SOURCE, encoding="utf-8")
            stdout, stderr, status = api.run([
                "--strict", "--python-version=3.10", "--no-incremental", "--follow-imports=silent", str(source_path),
            ])
        self.assertNotEqual(status, 0, stdout + stderr)
        self.assertIn("id", stdout + stderr)


if __name__ == "__main__":
    unittest.main()
