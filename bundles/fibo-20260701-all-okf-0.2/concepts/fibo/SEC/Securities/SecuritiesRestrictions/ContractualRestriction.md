---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual restriction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms setting out restrictions on either the holder or the issuer of the security, as specified in the
      terms of the instrument itself
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/ContractualRestriction
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: contractual restriction
type: Ontology Class
---

# contractual restriction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/ContractualRestriction>

## Definition

contract terms setting out restrictions on either the holder or the issuer of the security, as specified in the terms of the instrument itself

## Relationships

- **Subclass of**: [ContractualCommitment](/concepts/fibo/FND/Agreements/Contracts/ContractualCommitment.md)
- **Subclass of**: [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)

## Constraints

- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: all values from of type [Contract](/concepts/fibo/FND/Agreements/Contracts/Contract.md)

## Annotations

- **label**: contractual restriction
- **definition**: contract terms setting out restrictions on either the holder or the issuer of the security, as specified in the terms of the instrument itself

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
