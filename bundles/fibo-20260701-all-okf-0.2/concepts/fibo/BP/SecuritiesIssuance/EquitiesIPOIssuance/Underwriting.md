---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriting
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/PotentialShareUnderwriter
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/shareUnderwriter
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/SyndicateMember
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/syndicateMember
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/Underwriting
sources:
- id: fibo-source-fb4230f5b0
  resource: references/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
  sha256: fb4230f5b0812f53d30ce91b5b00a7d962d30b713eb159867935983fd6f7bbe7
  title: FIBO source BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
title: underwriting
type: Ontology Class
---

# underwriting

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/Underwriting>

## Constraints

- **[shareUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/shareUnderwriter.md)**: some values from of type [PotentialShareUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/PotentialShareUnderwriter.md)
- **[syndicateMember](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/syndicateMember.md)**: some values from of type [SyndicateMember](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/SyndicateMember.md)

## Annotations

- **label** (en): underwriting

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
