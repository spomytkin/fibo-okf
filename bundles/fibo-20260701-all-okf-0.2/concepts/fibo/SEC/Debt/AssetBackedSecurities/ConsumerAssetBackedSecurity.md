---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured finance securities collateralized by pools of auto loans and leases (auto ABS), credit card receivables
      (credit card ABS) or student loans (student loan ABS)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://content.naic.org/sites/default/files/capital-markets-primer-consumer-abs.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ConsumerAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: consumer asset-backed security
type: Ontology Class
---

# consumer asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ConsumerAssetBackedSecurity>

## Definition

structured finance securities collateralized by pools of auto loans and leases (auto ABS), credit card receivables (credit card ABS) or student loans (student loan ABS)

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Annotations

- **label** (en): consumer asset-backed security
- **definition** (en): structured finance securities collateralized by pools of auto loans and leases (auto ABS), credit card receivables (credit card ABS) or student loans (student loan ABS)
- **adaptedFrom**: https://content.naic.org/sites/default/files/capital-markets-primer-consumer-abs.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
