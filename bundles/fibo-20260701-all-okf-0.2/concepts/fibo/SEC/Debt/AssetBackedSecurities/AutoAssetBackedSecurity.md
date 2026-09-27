---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: auto asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security that is backed by an underlying pool of auto-related loans and/or leases
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://content.naic.org/sites/default/files/capital-markets-primer-auto-abs.pdf
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Auto asset-backed securities (auto ABS) are typically structured finance securities that are collateralized by
      auto loans or leases, such as those to prime (good credit standing) and subprime (poor credit standing) borrowers. Loans
      or leases are bundled into pools and transferred to a special-purpose entity (SPE), which, in turn, transfers the pool
      to a (bankruptcy remote) trust. Payments on the underlying auto loans and leases are pooled in the trust, and the funds
      are used to pay note investors their respective principal which, in turn, transfers the pool to a (bankruptcy remote)
      trust, i.e., one that protects the security from bankruptcy. Payments on the underlying auto loans and leases are pooled
      in the trust, and the funds are used to pay note investors their respective principal and interest when due. Any leftover
      funds - known as excess spread, or the net interest margin - are paid to the equity holder (usually the issuer, such
      as an auto finance company).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the credit risk of the pool has been decoupled from the institution via an SPV, then an auto asset-backed security
      is also a structured finance instrument.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoDebtPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: auto asset-backed security
type: Ontology Class
---

# auto asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoAssetBackedSecurity>

## Definition

asset-backed security that is backed by an underlying pool of auto-related loans and/or leases

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [AutoDebtPool](/concepts/fibo/SEC/Debt/AssetBackedSecurities/AutoDebtPool.md)

## Annotations

- **label** (en): auto asset-backed security
- **definition** (en): asset-backed security that is backed by an underlying pool of auto-related loans and/or leases
- **adaptedFrom**: https://content.naic.org/sites/default/files/capital-markets-primer-auto-abs.pdf
- **explanatoryNote** (en): Auto asset-backed securities (auto ABS) are typically structured finance securities that are collateralized by auto loans or leases, such as those to prime (good credit standing) and subprime (poor credit standing) borrowers. Loans or leases are bundled into pools and transferred to a special-purpose entity (SPE), which, in turn, transfers the pool to a (bankruptcy remote) trust. Payments on the underlying auto loans and leases are pooled in the trust, and the funds are used to pay note investors their respective principal which, in turn, transfers the pool to a (bankruptcy remote) trust, i.e., one that protects the security from bankruptcy. Payments on the underlying auto loans and leases are pooled in the trust, and the funds are used to pay note investors their respective principal and interest when due. Any leftover funds - known as excess spread, or the net interest margin - are paid to the equity holder (usually the issuer, such as an auto finance company).
- **explanatoryNote** (en): If the credit risk of the pool has been decoupled from the institution via an SPV, then an auto asset-backed security is also a structured finance instrument.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
